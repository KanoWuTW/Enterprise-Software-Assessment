document.getElementById("defaultpage").value = 1

// Track the current page number
let current_page = 1;

// Set the default page value for the search form (if present)
const defaultPageInput = document.getElementById("defaultpage");
if (defaultPageInput) {
    defaultPageInput.value = 1;
}

// Update the product list in the catalog
function updateList(data, catalog_list) {
    if (data.size === 0) return;
    const OldbasketBtn = catalog_list.querySelector(".btn.btn-success");
    const OldwishBtn = catalog_list.querySelector(".btn.btn-primary");
    catalog_list.innerHTML = "";

    for (let i = 0; i < data.size; i++) {
        const li = document.createElement("li");

        // Product name link
        const itemlink = document.createElement("a");
        itemlink.href = `/item?id=${data.ids[i]}`;
        itemlink.className = "itemLink";
        itemlink.textContent = data.products_names[i];

        // Category link
        const categoryLink = document.createElement("a");
        categoryLink.href = `/cat?id=${data.catids[i]}`;
        categoryLink.className = "categoryLink";
        categoryLink.textContent = data.product_categories[i];

        // Product price
        const price = document.createElement("span");
        price.textContent = "£" + data.product_prices[i];
        price.className = "price";

        // Product stock
        const stock = document.createElement("span");
        stock.textContent = "stock number: " + data.product_stocks[i];
        stock.className = "stock";

        // Add to basket button
        const basketBtn = document.createElement("button");
        basketBtn.type = OldbasketBtn.getAttribute("type");
        basketBtn.className = OldbasketBtn.getAttribute("class");
        basketBtn.textContent = "Add to basket";
        basketBtn.dataset.bsToggle = OldbasketBtn.dataset.bsToggle;
        basketBtn.dataset.bsTarget = OldbasketBtn.dataset.bsTarget;

        // Add to wishlist button
        const wishBtn = document.createElement("button");
        wishBtn.type = OldwishBtn.getAttribute("type");
        wishBtn.className = OldwishBtn.getAttribute("class");
        wishBtn.textContent = "Add to wishlist";
        wishBtn.dataset.bsToggle = OldwishBtn.dataset.bsToggle;
        wishBtn.dataset.bsTarget = OldwishBtn.dataset.bsTarget;

        // Append all elements to the list item
        li.appendChild(itemlink);
        li.appendChild(categoryLink);
        li.appendChild(price);
        li.appendChild(stock);
        li.appendChild(basketBtn);
        li.appendChild(wishBtn);

        catalog_list.appendChild(li);
    }
    bindButtons();
}


// Next page button event
document.getElementById("next_page").addEventListener("click", () => {
    fetch(`main-to?page=${current_page + 1}&cat=0`)
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw err; });
            }
            response.json().then(data => {
                if (data.size > 0) {
                    const catalog_list = document.getElementById("main-catalog");
                    updateList(data, catalog_list);
                    current_page += 1;
                    document.getElementById("page-index").textContent = current_page;
                }
            });
        })
        .catch(error => {
            console.error(error);
        });
});


// Previous page button event
document.getElementById("previous_page").addEventListener("click", () => {
    fetch(`main-to?page=${current_page - 1}&cat=0`)
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw err; });
            }
            response.json().then(data => {
                if (data.size > 0) {
                    const catalog_list = document.getElementById("main-catalog");
                    updateList(data, catalog_list);
                    current_page -= 1;
                    document.getElementById("page-index").textContent = current_page;
                }
            });
        })
        .catch(error => {
            console.error(error);
        });
});


bindButtons()

// Bind click events for basket and wishlist buttons
function bindButtons() {
    // Bind basket buttons
    document.querySelectorAll('.btn.btn-success.liveToastBtn').forEach(btn => {
        btn.addEventListener('click', () => {
            const li = btn.parentElement;
            const itemLink = li.querySelector(".itemLink");
            const url = new URL(itemLink.href, window.location.origin);
            const id = url.searchParams.get("id");
            const itemName = itemLink.textContent;
            fetch(`/item/addbasket?id=${id}`)
                .then(response => response.json())
                .then(data => {
                    const message = document.getElementById("toast-body");
                    if (data.in_stock) {
                        message.textContent = `${itemName} is successfully added to your basket!`;
                    } else {
                        message.textContent = `Cannot add ${itemName} to your basket!`;
                    }
                })
                .catch(error => { console.error(error); });
            const toastMsg = document.getElementById('liveToast');
            const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastMsg);
            toastBootstrap.show();
        });
    });
    // Bind wishlist buttons
    document.querySelectorAll('.btn.btn-primary.liveToastBtn').forEach(btn => {
        btn.addEventListener('click', () => {
            const li = btn.parentElement;
            const itemLink = li.querySelector(".itemLink");
            const url = new URL(itemLink.href, window.location.origin);
            const id = url.searchParams.get("id");
            const itemName = itemLink.textContent;
            fetch(`/item/addwishlist?id=${id}`)
                .then(response => response.json())
                .then(data => {
                    const message = document.getElementById("toast-body");
                    if (data.in_stock) {
                        message.textContent = `${itemName} is successfully added to your wishlist!`;
                    } else {
                        message.textContent = `Cannot add ${itemName} to your wishlist!`;
                    }
                })
                .catch(error => { console.error(error); });
            const toastMsg = document.getElementById('liveToast');
            const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastMsg);
            toastBootstrap.show();
        });
    });
}

// Initialize button bindings on page load
bindButtons();