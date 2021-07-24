<script>
	import { fly } from 'svelte/transition';
	import WeatherBox from "./weather_box.svelte";

	let city = "";

	let result = {};

	let success = false;

	let lastSearches = [];

	const handleKeyup = (event) => {
		if (event.code == "Enter") {
			event.preventDefault()
			success = undefined
			return false
		}
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
			value={city}
		/>
		<span>now?</span>
	</div>

	{#if success}
		<WeatherBox {result} />
	{/if}

	{#if success === undefined}
		<h2 class="error" transition:fly={{duration: 3000}}>Sorry. We couldn´t find the specified city.</h2>
	{/if}

	{#if lastSearches.length > 0}
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
