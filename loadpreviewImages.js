var previewsection = document.getElementById("carmodelspreview");
var array = []
var doc
var imagecol = document.createElement("div")
var allimages
var loadcommentsbutton = document.getElementById("loadcomments");
loadcommentsbutton.addEventListener("click", function () {
    loadmore();
    loadcommentsbutton.remove();
})



function loadmore() {
    axios.get('imageslinks.html')
        .then(function (response) {
            doc = new DOMParser().parseFromString(response.data, 'text/html');
            allimages = doc.body.querySelector("div[class=images]")
            imagecol = doc.body.querySelector("div[class=imagecol]")
            var i;
            for (i = 0; i < allimages.children.length; i++) {
                var image = allimages.children[i]
                array.push(image)
            }

        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            for (i = 0; i < array.length; i++) {
                var image = array[i]
                var imagecolcopy = imagecol.cloneNode(true);
                var card = imagecolcopy.querySelector("div[class=card]");
                card.innerHTML = null
                card.appendChild(image)
                previewsection.appendChild(imagecolcopy.children[0])
            }
            loadModal();
        });

}