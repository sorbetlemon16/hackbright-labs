"use strict";

const addItemToCart = (itemName) => {
  $('#cart-items').append(`
    <tr>
      <td>${itemName}</td>
    </tr>
  `);
};

const resetCart = () => {
  $('#cart-total').html('0.00');
  $('#cart-items').empty();
};

const incrementCartTotal = (price) => {
  const cartTotal = $('#cart-total');

  let total = Number(cartTotal.html());
  total += price;

  cartTotal.html(total.toFixed(2));
};

const incrementCoffeeSold = (amountSold) => {
  let coffeeSold = Number($('#coffee-sold-counter').html());
  coffeeSold += amountSold;

  $('#coffee-sold-counter').html(coffeeSold);
};

const setProgressAndStatus = (progressVal, statusMsg) => {
  $('#order-progress').attr('value', progressVal);
  $('#order-status-message').html(statusMsg);
};


//
// Add your event handlers below.
//


$('.add-to-order').on('click', () => {
  addItemToCart('Coffee');
  incrementCartTotal(1.50);
});

$('#place-order').on('click', () => {
  incrementCoffeeSold($('#cart-items').children().length);

  resetCart();

  setProgressAndStatus(0, 'We recieved your order!');

  setTimeout(() => {
    setProgressAndStatus(25, 'Grinding beans...');

    setTimeout(() => {
      setProgressAndStatus(50, 'Brewing coffee...');

      setTimeout(() => {
        setProgressAndStatus(75, 'Pouring coffee...');

        setTimeout(() => {
          setProgressAndStatus(100, 'Your coffee is on its way!');
        }, 1000);
      }, 1000);
    }, 1000);
  }, 1000);
});
