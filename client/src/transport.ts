class Transporter {

    private ws!: WebSocket;

    constructor() {

        // eslint-disable-next-line @typescript-eslint/no-this-alias
        const that = this;

        this.ws = new WebSocket(`ws://${window.location.hostname}:${11324}`);
        this.ws.onopen = () => this.start();
        this.ws.onmessage = ({ data }) => this.onMessage(data);
        this.ws.onclose = ()=>console.log("disconnected")
    }

    private async start() {
        console.log("connected")
        this.ws.send("helloasda")
        //this.ws.send(await this.getFrame() || "");
    }

    private async onMessage(data: Blob | string) {
        console.log(data)
        // if (this.onResult && typeof data !== "string")
        //     this.onResult(await createImageBitmap(data));

    }


    stop = () => {
        this.ws.close();
    }

}

export default Transporter;
