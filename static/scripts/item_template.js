// Set the default page value for pagination/search
document.getElementById("defaultpage").value = 1;

// Get item id from URL parameters
const params = new URLSearchParams(window.location.search);
const id = params.get("id");

// Get the item name from the DOM
const itemName = document.getElementById("name").textContent;

// Handle "Add to basket" button click
document.getElementById('basketBtn').addEventListener('click', () => {
    fetch(`/item/addbasket?id=${id}`)
        .then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    // Show success or failure message in toast
                    const message = document.getElementById("toast-body");
                    if (data.in_stock) {
                        message.textContent = `${itemName} is successfully added to your basket!`;
                    } else {
                        message.textContent = `Cannot add ${itemName} to your basket!`;
                    }
                });
            }
        })
        .catch((error) => {
            // Log any fetch errors
            console.error(error);
        });
    // Show toast notification
    try {
        const toastLiveExample = document.getElementById('liveToast');
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
        toastBootstrap.show();
    } catch (e) {
        // Ignore errors if toast cannot be shown
    }
});

// Handle "Add to wishlist" button click
document.getElementById('wishBtn').addEventListener('click', () => {
    fetch(`/item/addwishlist?id=${id}`)
        .then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    // Show success or failure message in toast
                    const message = document.getElementById("toast-body");
                    if (data.in_stock) {
                        message.textContent = `${itemName} is successfully added to your wishlist!`;
                    } else {
                        message.textContent = `Cannot add ${itemName} to your wishlist!`;
                    }
                });
            }
        })
        .catch((error) => {
            // Log any fetch errors
            console.error(error);
        });
    // Show toast notification
    try {
        const toastLiveExample = document.getElementById('liveToast');
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
        toastBootstrap.show();
    } catch (e) {
        // Ignore errors if toast cannot be shown
    }
});
