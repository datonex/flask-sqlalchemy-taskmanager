$(document).ready(function () {
  // sidenav initialization
  $('.sidenav').sidenav();
  // datepicker initialization
  $('.datepicker').datepicker({
    format: 'dd mmm yyyy',
    i18n: { done: 'Select' },
  });
  // select initialization
  $('select').formSelect();
});
