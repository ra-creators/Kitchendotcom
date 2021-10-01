console.log('hei')
var container = "#carouselExampleCaptions";
var dir = "static/design%20gallery/img/gallery/Kitchen/";
var fileextension = ".svg";
var page = 0;
var numberItemPerPage = Math.floor(($("#fourth .carousel-inner").width() - 200) / 300) * 2 | 2;
// console.log(numberItemPerPage)
let pageItems = [];
// console.log(container)

function newPage(pageNumber) {
  $(`${container} .carousel-indicators`).append(
    `<button
    type="button"
    data-bs-target="#carouselExampleCaptions"
    data-bs-slide-to="${pageNumber-1}"
    ${pageNumber===1?"class=\"active\"":""}
    aria-current="true"
    aria-label="Page ${pageNumber}"
    ></button>`
  )

  $(`${container} .carousel-inner`).append(
    `
      <div class="carousel-item ${pageNumber===1?"active":""}">
        <div class="decorators">
          <div class="bg-holder">
            <svg
              viewBox="0 0 1440 1251"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M0 0C618.7 258.103 963.357 237.595 1460 0V1251H0V0Z"
                fill="#E8F2F2"
              />
            </svg>
          </div>
          <div class="item-2">
            <img src="/static/design gallery/img/gallery_topleft.png" alt="" />
          </div>
          <div class="item-0">
            <img src="/static/design gallery/img/gallery_0.svg" alt="" />
          </div>
          <div class="item-1">
            <img src="/static/design gallery/img/gallery_1.svg" alt="" />
          </div>
        </div>
        <div
        id=\"page-${pageNumber}\"
        class="gallery-container carousel slide"
        data-bs-ride="carousel"
        >        
        </div>
      </div>
      `
  )
}

for (let i = 1; i <= 50; i++) {
  // console.log(i);
  var filename = i + fileextension;

  if (i % numberItemPerPage === 1 || numberItemPerPage === 1) {
    ++page;
    // if(page===2)
    // break;
    newPage(page);
  }
  // console.log(filename)
  $(`#page-${page}`).append(
    `
            <img
            src="${dir + filename}"
            alt=""
            class="card-img-top"
            style="background-color:transparent;"
            />
      `
  )

}

$(`${container} .carousel-inner`).append(
  `
  <button
  class="carousel-control-prev"
  type="button"
  data-bs-target="#carouselExampleCaptions"
  data-bs-slide="prev"
>
  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
  <span class="visually-hidden">Previous</span>
</button>
<button
  class="carousel-control-next"
  type="button"
  data-bs-target="#carouselExampleCaptions"
  data-bs-slide="next"
>
  <span class="carousel-control-next-icon" aria-hidden="true"></span>
  <span class="visually-hidden">Next</span>
</button>
  `
)