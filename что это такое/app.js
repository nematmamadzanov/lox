/* Created by Tivotal */

const closer = document.querySelector("#closer");
closer.onclick = ()=>{
    closer.style.display = "none";
    navBar.classList.remove("active")
}

const navBar = document.querySelector(".navbar");
document.querySelector("#menu-btn").onclick = () => {
    closer.style.display = "block";
    navBar.classList.toggle("active")
};