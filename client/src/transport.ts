class Transporter {

    private ws!: WebSocket;
    private onMessageCB: (data: Blob, f: boolean) => void;
    private flag: boolean;

    constructor(onMessageCB: (data: Blob, f: boolean) => void) {

        // eslint-disable-next-line @typescript-eslint/no-this-alias
        const that = this;
        this.flag = false;
        this.onMessageCB = onMessageCB;
        this.ws = new WebSocket(`ws://${window.location.hostname}:${11324}`);
        this.ws.onopen = () => this.start();
        this.ws.onmessage = ({ data }) => this.onMessage(data);
        this.ws.onclose = () => console.log("disconnected")

    }

    private async start() {
        console.log("connected")
        this.ws.send("helloasda")
        //this.ws.send(await this.getFrame() || "");
    }

    private async onMessage(data: Blob | string) {
        if (this.onMessageCB && typeof data !== "string"){
            this.flag=!this.flag;
            this.onMessageCB(data, this.flag);
        }
    }


    stop = () => {
        this.ws.close();
    }

}

export default Transporter;
