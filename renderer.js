const image_input = document.querySelector("#image_input")
var uploaded_image = ""
image_input.addEventListener("change", function() {
    console.log(image_input.files[0].path)
    const reader = new FileReader()
    reader.addEventListener("load", () => {
        const uploaded_image = reader.result
        document.querySelector("#original-image").style.backgroundImage = `url(${uploaded_image})`
    })
    reader.readAsDataURL(this.files[0])
})