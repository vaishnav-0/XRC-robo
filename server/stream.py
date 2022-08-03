import pyrealsense2 as rs
import numpy as np
import time
import asyncio


class RealsenseStream:

    def __init__(self):
        print("reset start")
        ctx = rs.context()
        devices = ctx.query_devices()
        for dev in devices:
            dev.hardware_reset()
        print("reset done")
        device_id = None  # "923322071108" # serial number of device to use or None to use default
        self.enable_imu = True
        self.enable_rgb = True
        self.enable_depth = True
        # TODO: enable_pose
        # TODO: enable_ir_stereo


        # Configure streams

        self.imu_config = rs.config()
        self.imu_config.enable_stream(rs.stream.accel) # acceleration
        self.imu_config.enable_stream(rs.stream.gyro)  # gyroscope


        self.config = rs.config()
            # if we are provided with a specific device, then enable it
        if None != device_id:
            self.config.enable_device(device_id)

        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 60)  # depth
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 60)  # rgb
        self.pipeline = None
        self.imu_pipeline = None
    
    def start_stream(self,queue):
        print("starting streaming")
        self.pipeline = rs.pipeline()
        profile = self.pipeline.start(self.config)
        self.imu_pipeline = rs.pipeline()
        imu_profile = self.imu_pipeline.start(self.imu_config)


        # Getting the depth sensor's depth scale (see rs-align example for explanation)
        depth_sensor = profile.get_device().first_depth_sensor()
        depth_scale = depth_sensor.get_depth_scale()

        print("Depth Scale is: ", depth_scale)
            # Create an align object
            # rs.align allows us to perform alignment of depth frames to others frames
            # The "align_to" is the stream type to which we plan to align depth frames.

        align_to = rs.stream.color
        align = rs.align(align_to)	

        while True: 
            frames = self.pipeline.wait_for_frames() # wait 10 seconds for first frame
            imu_frames = self.imu_pipeline.wait_for_frames()

            # Align the depth frame to color frame
            aligned_frames = align.process(frames) if self.enable_depth and self.enable_rgb else None
            depth_frame = aligned_frames.get_depth_frame() if aligned_frames is not None else frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame() if aligned_frames is not None else frames.get_color_frame()
            # Convert images to numpy arrays
            depth_image = np.asanyarray(depth_frame.get_data()) if self.enable_depth else None
            color_image = np.asanyarray(color_frame.get_data()) if self.enable_rgb else None
            # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
            # Stack both images horizontally
            images = None
            if(queue):
                queue.put(color_image.tobytes())
            #print("depth infromation",depth_image)
            #print("color_image",color_image)
            # Show images
            # accel_frame = imu_frames.first_or_default(rs.stream.accel, rs.format.motion_xyz32f)
            # gyro_frame = imu_frames.first_or_default(rs.stream.gyro, rs.format.motion_xyz32f)
            #print("imu \n\taccel = {}, \n\tgyro = {}".format(str(accel_frame.as_motion_frame().get_motion_data()), str(gyro_frame.as_motion_frame().get_motion_data())))
    
    
    def stop_stream(self):
        # Stop streaming
        if(self.pipeline):
            self.pipeline.stop()
        if(self.imu_pipeline):
            self.imu_pipeline.stop()
