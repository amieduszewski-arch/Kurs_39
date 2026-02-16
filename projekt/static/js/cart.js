async function addToCart(productName) {

    await fetch("/add-to-cart", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `product=${encodeURIComponent(productName)}`
    });

    openSideCart();
}


async function openSideCart() {

    const response = await fetch("/cart-data");
    const data = await response.json();

    const cartBox = document.getElementById("cart-items");

    cartBox.innerHTML = "";

    data.items.forEach((item, index) => {
        cartBox.innerHTML += `
            <div class="cart-item">
                ${item.name} - ${item.price} zł
                <button onclick="removeFromCart(${index})" class="remove-mini">✕</button>
            </div>
        `;
    });

    document.getElementById("cart-total").innerText = data.total;
    document.getElementById("cart-discount").innerText = data.discount;
    document.getElementById("cart-final").innerText = data.final_price;

    document.getElementById("side-cart").classList.add("active");
    document.getElementById("cart-overlay").classList.add("active");
    document.body.classList.add("cart-open");
}


document.addEventListener("DOMContentLoaded", () => {

    const overlay = document.getElementById("cart-overlay");
    const sideCart = document.getElementById("side-cart");

    if (!overlay || !sideCart) return;

    overlay.addEventListener("click", () => {
        sideCart.classList.remove("active");
        overlay.classList.remove("active");
        document.body.classList.remove("cart-open");
    });

});


async function removeFromCart(index) {

    await fetch("/remove-from-cart-ajax", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `index=${index}`
    });

    openSideCart();
}