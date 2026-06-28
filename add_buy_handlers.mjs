const fs = require('fs');
let js = fs.readFileSync('app.js', 'utf8');

const buyBtnHandler = `
// Stripe Buy Now buttons - CSP-safe event delegation
document.addEventListener('click', function(e) {
  var btn = e.target.closest('[data-package]');
  if (btn && btn.classList.contains('btn-primary')) {
    e.preventDefault();
    var pkg = btn.getAttribute('data-package');
    var price = btn.getAttribute('data-price');
    var msg = 'Payment processing will be available once Stripe is connected. Contact sales@leadsqualiflow.com to purchase the ' + pkg + ' package (' + price + ').';
    if (typeof announce === 'function') announce(msg);
  }
});
`;

if (js.indexOf('data-package') === -1) {
  js = js.replace('console.log', buyBtnHandler + 'console.log');
  fs.writeFileSync('app.js', js);
  console.log('Buy Now handlers added');
} else {
  console.log('Buy Now handlers already exist');
}

// Verify syntax
try {
  require('node:vm').compileFunction(js);
  console.log('JS syntax OK');
} catch(e) {
  console.log('Syntax error:', e.message);
}
