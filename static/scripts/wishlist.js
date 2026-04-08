// Set the default page value for search/pagination
document.getElementById("defaultpage").value = 1;

function bindBaketBtns() {
    const ul = document.getElementById("wishlist");
    ul.querySelectorAll("li").forEach(li => {
        // Get the product id from the link
        const url = new URL(li.querySelector("a").href);
        const params = new URLSearchParams(url.search);
        // Add click event to the remove button
        li.querySelector(".btn.btn-success").addEventListener("click", () => {
            fetch(`/item/addbasket?id=${params.get("id")}`)
                .then((response) => {
                    response.json().then((data) => {
                        if (data.in_stock) {
                            console.log("successfully added to basket.")
                        }
                    });
                });
        });
    });
}


// Bind click events for all "Remove from wishlist" buttons
function bindRemoveBtns() {
    const ul = document.getElementById("wishlist");
    ul.querySelectorAll("li").forEach(li => {
        // Get the product id from the link
        const url = new URL(li.querySelector("a").href);
        const params = new URLSearchParams(url.search);
        // Add click event to the remove button
        li.querySelector(".removeBtn").addEventListener("click", () => {
            fetch(`/user/wishlist/remove?id=${params.get("id")}`)
                .then((response) => {
                    response.json().then((data) => {
                        // Remove the item from the DOM if successfully removed
                        if (data.removed) {
                            li.remove();
                        }
                    });
                });
        });
    });
}

// Initial binding for page load
bindRemoveBtns();
bindBaketBtns()