import Transporter from "./transport.js";
const rgbCtx = document.getElementById("rgbCanvas").getContext("2d");
const depthCtx = document.getElementById("depthCanvas").getContext("2d");
const onMessage = async (data, f) => {
    const image = await createImageBitmap(data);
    if (image) {
        if (f) {
            if (!rgbCtx)
                return;
            rgbCtx.clearRect(0, 0, rgbCtx.canvas.width, rgbCtx.canvas.height);
            rgbCtx.drawImage(image, 0, 0, rgbCtx.canvas.width, rgbCtx.canvas.height);
        }
        else {
            if (!depthCtx)
                return;
            depthCtx.clearRect(0, 0, depthCtx.canvas.width, depthCtx.canvas.height);
            depthCtx.drawImage(image, 0, 0, depthCtx.canvas.width, depthCtx.canvas.height);
        }
    }
};
const trans = new Transporter(onMessage);
//# sourceMappingURL=index.js.map