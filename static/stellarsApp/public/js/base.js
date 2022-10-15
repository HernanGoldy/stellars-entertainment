

let arrow = document.querySelectorAll(".arrow");

for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e) => {
        let arrowParent = e.target.parentElement.parentElement;
        arrowParent.classList.toggle("showMenu");
	});
}

let sidebar = document.querySelector(".sidebar");
console.log(sidebar);
sidebar.addEventListener("mouseover", () => {
    let showSidebar = document.querySelector(".ul");
    sidebar.classList.add("show");
});

sidebar.addEventListener("mouseout", () => {
    let showSidebar = document.querySelector(".ul");
    sidebar.classList.remove("show");
})
