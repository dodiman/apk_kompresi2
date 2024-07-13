const url = new URL(window.location.href);
const base_url = `${url.protocol}//${url.hostname}${url.port ? ':' + url.port : ''}`;

// console.log(base_url);