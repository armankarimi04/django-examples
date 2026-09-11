import "@/css/main.css";
import htmx from "htmx.org";
import Alpine from "alpinejs";

window.Alpine = Alpine;
Alpine.start()

window.htmx = htmx;

console.log('main.js - ok');