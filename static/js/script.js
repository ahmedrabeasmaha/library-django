try {
    document.getElementById("id_return_date").min = new Date().getFullYear() + "-" +  parseInt(new Date().getMonth() + 1 ) + "-" + parseInt(new Date().getDate() + 1 );
} catch (e) {
}