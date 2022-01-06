// // Actions:

// const closeButton = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
// <title>remove</title>
// <path d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"></path>
// </svg>
// `;
// const menuButton = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
// <title>ellipsis-horizontal</title>
// <path d="M16 7.843c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 1.98c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// <path d="M16 19.908c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 14.046c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// <path d="M16 31.974c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 26.111c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// </svg>
// `;

// const actionButtons = document.querySelectorAll('.action-button');

// if (actionButtons) {
//   actionButtons.forEach(button => {
//     button.addEventListener('click', () => {
//       const buttonId = button.dataset.id;
//       let popup = document.querySelector(`.popup-${buttonId}`);
//       console.log(popup);
//       if (popup) {
//         button.innerHTML = menuButton;
//         return popup.remove();
//       }

//       const deleteUrl = button.dataset.deleteUrl;
//       const editUrl = button.dataset.editUrl;
//       button.innerHTML = closeButton;

//       popup = document.createElement('div');
//       popup.classList.add('popup');
//       popup.classList.add(`popup-${buttonId}`);
//       popup.innerHTML = `<a href="${editUrl}">Edit</a>
//       <form action="${deleteUrl}" method="delete">
//         <button type="submit">Delete</button>
//       </form>`;
//       button.insertAdjacentElement('afterend', popup);
//     });
//   });
// }

// Menu

const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;


//get the data stored in the localStorage for display on load
function getLists() {
  if(localStorage.getItem("feedroom") === null){
    alert("Your dashboard is currently empty. Use the add button to add new products.");
    document.getElementById("search").disabled = true;
  } else {
    //document.getElementById("search").disabled = false;
    let feedrooms = JSON.parse(localStorage.getItem("feedroom"));
    console.log(feedrooms);
   // let productDisplay = document.getElementById('productDisplay');
    //Display result
    // productDisplay.innerHTML = '';
    // for (let i = 0; i < productList.length; i++){
    //   let id = productList[i].id;
    //   let name = productList[i].name;
    //   let category = productList[i].category;
    //   let description = productList[i].description;

    //   productDisplay.innerHTML += '<li class="list-group-item"><strong>'+name+'</strong><p>'+category+'</p><p>'+description+'</p><p><a' +
    //       ' href="#" onclick="editProduct(\''+id+'\')" data-toggle="modal" data-target="#addNewProductModal">' +
    //       '<i class="fa fa-edit green-text darken-2 "></i>&nbsp;Edit</a> &nbsp;&nbsp; ' +
    //       '<a href="#" id="deleteId" onclick="deleteProduct(\''+id+'\')"><i class="fa fa-trash' +
    //       ' red-text' +
    //       ' darken-2"></i>&nbsp;' +
    //       ' Delete</a>' +
    //       ' </p>' +
    //       '</li>';
    //   }
    }
  }


// deleting the main bookmark.
function deleteProduct(id) {
  let productList = JSON.parse(localStorage.getItem("productList"));
  for(let i = 0; i < productList.length; i++){
    if (productList[i].id === id) {
      productList.splice(i,1);
      //console.log(result);
    }
  }
  localStorage.setItem("productList", JSON.stringify(productList)); //reset the values in the local storage
  getProductLists(); // to quickly display what is remaining from local storage.
}

// Editing a product
function editProduct(id) {
  "use strict";
  document.getElementById('modalSubmit').style.display = "none";
  document.getElementById("addNewProductModalLabel").textContent = "Edit Product";

  let tempId = id;
  let parentDiv = document.getElementById('modalFooter');
  let productList = JSON.parse(localStorage.getItem("productList"));


  if (parentDiv.contains(document.getElementById("editButton"))) {
    document.getElementById('editButton').disabled = false;
  } else {
    let editButton = document.createElement('button');
    editButton.id = "editButton";
    editButton.className = "fa fa-hdd-o btn btn-outline-primary btn-sm m-2";
    editButton.textContent = " Save data";
    parentDiv.appendChild(editButton);
  }
  for (let i = 0; i < productList.length; i++) {
    if (productList[i].id === id) {
      document.getElementById("productName").value = productList[i].name;
      document.getElementById("productDescription").value = productList[i].description;
      document.getElementById("productCategory").value = productList[i].category;
    }
  }

  document.getElementById("editButton").addEventListener("click", function () {
    addProduct();
    let productList = JSON.parse(localStorage.getItem("productList"));
    for(let i = 0; i < productList.length; i++){
      if(productList[i].id === tempId){
        productList.splice(i,1);
      }
    }
    localStorage.setItem("productList", JSON.stringify(productList));
    getProductLists();
    resetForm();
    document.getElementById("editButton").style.display = "none";

    $(".addNewProduct").on('click',productFormReset());

  });

}

function resetForm() {
  document.getElementById("productName").value = "";
  document.getElementById("productDescription").value = "";
  document.getElementById("productCategory").value = "";
}

function productFormReset() {
  document.getElementById('modalSubmit').style.display = "block";
  document.getElementById("addNewProductModalLabel").textContent = "New Product Form";
  document.getElementById('editButton').style.display = "none";
}