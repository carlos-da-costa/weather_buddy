<script>
	import { fly } from 'svelte/transition';
	import WeatherBox from "./weather_box.svelte";

	let city = "";

	let result = {};

	let success = false;

	let lastSearches = [];

	const handleKeyup = (event) => {
		if ((city === "") && (success === undefined)){
			success = false
			return
		}
		if (event.code == "Enter") {
			event.preventDefault()
			if (city === ""){
				success = false
			}
			else {
				getWeather(city)
			}
			
			return false
		}
	}

	async function getWeather(city_name) {
		fetch('http://127.0.0.1:5000/weather/' + city_name).then(response => {
			if (response.status === 200){
				response.json().then(d => {
					result = d
					result = result
					success = true
				})
			}
			else {
				result = {}
				success = undefined
			}
		})
		
		fetch('http://127.0.0.1:5000/weather?max_number=5').then(response => {
			if (response.status === 200){
				response.json().then(d => {
					lastSearches = d
					lastSearches = lastSearches
				})
			}
			else {
				lastSearches = []
			}
		})
	}

</script>

<header>
	<h1 class="title">WEATHER BUDDY</h1>
</header>
<main>
	<div id="search">
		<span>How is the weather in</span>
		<input
			id="city"
			class="city"
			placeholder="City"
			on:keyup={handleKeyup}
			bind:value={city}
		/>
		<span>now?</span>
	</div>
	
	{#if success}
		<div transition:fly={{duration: 3000}}>
			<WeatherBox {result} />
		</div>
	{/if}

	{#if success === undefined}
		<h2 class="error" transition:fly={{duration: 3000}}>Sorry. We couldn´t find the specified city.</h2>
	{/if}

	{#if (success !== undefined) & (lastSearches.length > 0)}
		<div class="last-searches" transition:fly={{duration: 3000}}>
			{#each lastSearches as search}
				<WeatherBox result={search} />
			{/each}
		</div>
	{/if}
	
</main>

<style>
	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		text-align: center;
		height: calc(100% - 8px);
		margin: 0px;
		padding: 0px;
	}

	header {
		text-align: center;
	}

	.title {
		color: black;
		font-size: 3em;
		font-weight: 300;
		border-bottom-color: balck;
		border-bottom-width: 1px;
		border-bottom-style: solid;
		width: 70%;
		margin-left: auto;
		margin-right: auto;
	}

	.error {
		color: red;
	}

	#city {
		min-width: 50px;
		width: max-content;
		display: inline-block;
		text-align: left;
		white-space: nowrap;
		overflow: hidden;
		text-transform: capitalize;
	}

	.city {
		position: relative;
		outline-width: 0;
		min-height: 1em;
		max-height: 300px;
		line-height: 1em;
		padding: 10px;
		word-wrap: break-word;
		border: 0px solid black;
		border-bottom-width: 1px;
		border-bottom-style: solid;
	}

	#search {
		font-size: 1.2em;
		top: 50%;
		margin-top: -15%;
	}

	.last-searches {
		display: flex;
		align-items: center;
		justify-content: space-around;
		flex-direction: row;
		background-color: #eff;
		height: 200px;
		width: 80%;
		margin-top: 5%;
	}
</style>
