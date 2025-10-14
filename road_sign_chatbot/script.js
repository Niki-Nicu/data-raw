const openBtn = document.getElementById("open-chat-btn");
const chatWidget = document.getElementById("chat-widget");
const closeBtn = document.getElementById("close-btn");
const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

// Open/Close Chat
openBtn.addEventListener("click", () => chatWidget.classList.add("open"));
closeBtn.addEventListener("click", () => chatWidget.classList.remove("open"));

// Send message
sendBtn.addEventListener("click", handleSend);
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") handleSend();
});

function handleSend() {
    const message = userInput.value.trim();
    if (!message) return;

    appendMessage(message, "user", "user.png");
    userInput.value = "";

    appendTyping();

    setTimeout(() => {
        removeTyping();
        const botReply = "Bot reply will appear here after training.";
        appendMessage(botReply, "bot", "bot.png");
        playSound();
    }, 1000);
}

// Append user/bot message
function appendMessage(text, sender, avatar = null) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", sender);

    if (avatar) {
        const img = document.createElement("img");
        img.src = avatar;
        msgDiv.appendChild(img);
    }

    const textNode = document.createTextNode(text);
    msgDiv.appendChild(textNode);

    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Typing animation
function appendTyping() {
    const typingDiv = document.createElement("div");
    typingDiv.classList.add("message", "bot");
    typingDiv.id = "typing-msg";

    const typingAnimation = document.createElement("div");
    typingAnimation.classList.add("typing");
    typingAnimation.innerHTML = `<span></span><span></span><span></span>`;

    typingDiv.appendChild(typingAnimation);
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
    const typing = document.getElementById("typing-msg");
    if (typing) typing.remove();
}

// Sound effect
function playSound() {
    const audio = new Audio("ping.mp3"); // add ping.mp3 in same folder
    audio.play();
}

// Make chat widget draggable
chatWidget.onmousedown = function(event) {
    let shiftX = event.clientX - chatWidget.getBoundingClientRect().left;
    let shiftY = event.clientY - chatWidget.getBoundingClientRect().top;

    function moveAt(pageX, pageY) {
        chatWidget.style.left = pageX - shiftX + 'px';
        chatWidget.style.top = pageY - shiftY + 'px';
    }

    function onMouseMove(event) {
        moveAt(event.pageX, event.pageY);
    }

    document.addEventListener('mousemove', onMouseMove);

    chatWidget.onmouseup = function() {
        document.removeEventListener('mousemove', onMouseMove);
        chatWidget.onmouseup = null;
    };
};

chatWidget.ondragstart = function() {
    return false;
};
