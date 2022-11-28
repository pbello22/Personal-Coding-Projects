async function fetchData()
{
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': 'ee0861370fmsh18f5de1866a60d5p19df3fjsnd999531152b4',
            'X-RapidAPI-Host': 'concerts-artists-events-tracker.p.rapidapi.com'
        }
    };
    
    const res = await fetch('https://concerts-artists-events-tracker.p.rapidapi.com/location?name=New%20York%20City&minDate=2022-05-20&maxDate=2022-11-26&page=1', options)
    const record = await res.json()
    
    console.log('record', record)

    document.getElementById("concerts").innerHTML = record.data.map(item => "<li>item.name</li>").join('');
}
fetchData();
