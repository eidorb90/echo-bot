const abortController = new AbortController();
let requestInFlight = undefined;
 
function main() {
    const input = document.querySelector("#echo_input");
    const output = document.querySelector("#output");

    input.addEventListener("change", async() => {
        if(requestInFlight) {
            abortController.abort("new request");
        }   

        const url = "https://echo-bot-shy-sea-4425.fly.dev/echo"
        requestInFlight = true;

        try {
            const response = await fetch(url, {
                method: "POST", 
                headers: {"Content-Type": "application/json"}, 
                body: JSON.stringify({ text: input.value }),
                signal: abortController.signal
            });

            if (response.ok) {
                const data = await response.json();
                output.innerHTML = data.text;
            }

        } catch (error) {
            if (error === "AbortError") {
                console.log("Request aborted");
                output.innerHTML = "<span style='color: orange'>Request aborted: A new request was made</span>";
            } else {
                console.log("Error: ", error);
                output.innerHTML = `<span style='color: red'>Error: ${error.message || error}</span>`;
            }
        }
    });
}    

document.addEventListener("DOMContentLoaded", main)