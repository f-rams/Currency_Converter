//USING JAVASCRIPT AXIOS (ALTERNATIVE OPTION)

// resultSection = $('#coverted-result');

// $('form').on('submit', async function (evt) {
//   evt.preventDefault();
//   fromValue = $('#from-value').val();
//   toValue = $('#to-value').val();
//   inputValue = $('#input-value').val();
//   res = await convert(fromValue, toValue, inputValue);
//   $(resultSection).append(
//     `<h2>Your converted value is <input type="text" disabled value="${res} ${toValue}" /></h2>`
//   );
//   this.reset();
// });

// async function convert(from, to, value) {
//   const res = await axios({
//     method: 'GET',
//     url: 'https://api.exchangerate.host/convert',
//     params: {
//       from: from,
//       to: to,
//       amount: value,
//     },
//   });
//   return res.data.result;
// }
