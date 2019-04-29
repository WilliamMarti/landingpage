var submitbutton = new Vue({
  delimiters: ['[[', ']]'],
  el: '#submitbutton',
  methods: {
      submit: function(name) {
          console.log('Ticket Number: ' + inputapp.ticketnumber)
      }
  }
});


var inputapp = new Vue({
  el: '#inputapp',
  data: {
      ticketnumber: ''
  }
});


