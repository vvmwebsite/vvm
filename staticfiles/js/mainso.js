console.log("JS loaded");
function toggleDark() {
    document.body.classList.toggle("dark");

    // Save theme for this session only
    if (document.body.classList.contains("dark")) {
        sessionStorage.setItem("theme", "dark");
    } else {
        sessionStorage.removeItem("theme");
    }
}

// Apply theme when page loads
window.onload = function() {
    if (sessionStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark");
    }
};


function openVideo(url) {
  document.getElementById("videoPopup").style.display = "flex";
  document.getElementById("popupVideo").src = url + "?autoplay=1";
}

function closeVideo() {
  document.getElementById("videoPopup").style.display = "none";
  document.getElementById("popupVideo").src = "";
}





const channelId = "UCY5-HuOOaR9yNiE-KW6pKaw";
const apiKey = "YOUR_API_KEY";
const channelUrl = "https://youtube.com/@vvmgospelmedia7399?si=9vZDwkvj5EeXndX6";

fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=${channelId}&eventType=live&type=video&key=${apiKey}`)
.then(res => res.json())
.then(data => {
    if (data.items && data.items.length > 0) {
        let liveId = data.items[0].id.videoId;
        document.getElementById("liveFrame").src =
            `https://www.youtube.com/embed/${liveId}?autoplay=1`;
    } else {
        document.getElementById("liveFrame").src =
            "https://www.youtube.com/embed?listType=user_uploads&list=@vvmgospelmedia7399?si=9vZDwkvj5EeXndX6";
    }
});


