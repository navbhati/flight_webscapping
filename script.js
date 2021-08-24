const search = document.getElementById('search')
const matchList = document.getElementById('match-list')


const searchAirports = async searchText => {
  const res = await fetch('airports.json')
  const state = await res.json();

  let matches = state.filter(state =>{
    const regex = new RegExp(`^${searchText}`, 'gi');
    return state.iata.match(regex);
  });

  if (searchText.length === 0){
    matches = [];
    matchList.innerHTML = '';
  }


  outputHtml(matches);
};

const outputHtml = matches => {
  if (matches.length > 0){
    const html = matches.map (
    match => `
    <div class="card card-body mb-1">
      <h4>${match.iata} (${match.name})</h4>
    </div>  

    `
    )
    .join('');
    
    matchList.innerHTML = html;
  }
}
search.addEventListener('input', () => searchAirports(search.value));

//|| state.name.match(regex);