<script>
    export let result
</script>

<div class="result">
    <span class="city-name">{result.city_name}</span>
    <span class="temperature">{result.temperature}°C</span>
    <span class="weather">{result.weather}</span>
</div>


<style>
    .city-name {
		font-weight: 500;
	}

	.temperature {
		font-size: 3em;
		font-weight: 500;
	}

	.weather {
		font-weight: 500;
        text-transform: capitalize;
	}

	.result {
        background-color: white;    
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-evenly;
		width: 150px;
		height: 150px;
		box-shadow: 0px 3px #ccc;
		border-radius: 4px;
	}
</style>