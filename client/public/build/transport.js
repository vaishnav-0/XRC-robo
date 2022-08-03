class Transporter {
    ws;
    constructor() {
        const that = this;
        this.ws = new WebSocket(`ws://${window.location.hostname}:${11324}`);
        this.ws.onopen = () => this.start();
        this.ws.onmessage = ({ data }) => this.onMessage(data);
        this.ws.onclose = () => console.log("disconnected");
    }
    async start() {
        console.log("connected");
        this.ws.send("helloasda");
    }
    async onMessage(data) {
        console.log(data);
    }
    stop = () => {
        this.ws.close();
    };
}
export default Transporter;
//# sourceMappingURL=transport.js.map