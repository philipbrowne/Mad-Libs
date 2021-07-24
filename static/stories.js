form = document.getElementById('storyform');
input = document.getElementById('storyselect');

input.addEventListener('change', (event) => {
  form.setAttribute('action', `/${input.value}`);
});
