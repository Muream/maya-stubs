const search_input = document.getElementById("search");
const search_results_div = document.querySelector(".search-results");

const trigger_search = () => {
  console.log("Search Triggered");
  search_results_div.style.opacity = 1;
  search_doc(search_input.value);
};

const validate_search = () => {
  console.log("Search Validated");
  if (search_input.value.length === 0) {
    cancel_search();
  }
};

const cancel_search = () => {
  console.log("Search Cancelled");
  search_results_div.style.opacity = 0;
  search_results_div.innerHTML = "";
};

const search_doc = (search_text) => {
  const search_options = {
    includeScore: true,
    keys: ["title"],
  };
  const search_index = Object.values(window.searchIndex.documentStore.docs);
  const fuse = new Fuse(search_index, search_options);

  let results = fuse.search(search_text);

  if (search_text.length === 0) {
    results = [];
  }

  generate_html(results.slice(0, 10));
};

const generate_html = (results) => {
  const html = results
    .map(
      (result) => `
      <div class="card card-body">
        <a href=\"${result.item.id}\">${result.item.title}</h4>
      </div>
    `
    )
    .join("");
  search_results_div.innerHTML = html;
};

search_input.addEventListener("input", () => trigger_search());
search_input.addEventListener("focusin", () => trigger_search());
search_input.addEventListener("search", () => validate_search());
// search_input.addEventListener("focusout", () => cancel_search());
