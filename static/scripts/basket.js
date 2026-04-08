// Set the default page value for the search form (if present)
const defaultPageInput = document.getElementById("defaultpage");
if (defaultPageInput) {
    defaultPageInput.value = 1;
}

// Bind remove button click events for all basket items
function bindRemoveBtns() {
    const ul = document.getElementById("basket");
    if (!ul) return; // Exit if basket list is not found

    ul.querySelectorAll("li").forEach(li => {
        // Get the product id from the item link
        const url = new URL(li.querySelector("a").href);
        const params = new URLSearchParams(url.search);
        const removeBtn = li.querySelector(".btn.btn-warning.removeBtn");
        if (!removeBtn) return;

        // Add click event to remove item from basket
        removeBtn.addEventListener("click", () => {
            fetch(`/user/basket/remove?id=${params.get("id")}`)
                .then(response => response.json())
                .then(data => {
                    if (data.removed) {
                        li.remove(); // Remove item from DOM if successfully deleted
                    }
                });
        });
    });
}

// Initialize remove button bindings on page load
bindRemoveBtns();