<script>

let city = 'pains'

const handleKeyup = (event) => {
		console.log
		if (event.code == 'Enter') {
			event.preventDefault()
			console.log('ahah')
			return false
		}
	}

</script>

<main>
	<h1>WEATHER BUDDY</h1>
	<div id="search">
		<span>How is the weather in</span>
		<input
			id="city"
			class="city"
			placeholder="City"
			on:keyup={handleKeyup}
			value={city}
		>
		<span>now?</span>
	</div>
	<div class="result">
		<span class="city-name">Florianópolis</span>
		<span class="temperature">22°C</span>
		<span class="weather"></span>
	</div>
</main>

<style>
	body {
		margin: 0px;
		padding: 0px;
	}

	main {
		text-align: center;
		height: calc(100% - 8px);
		margin: 0px;
		padding: 0px;
	}

	h1 {
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
		font-size: 2em;
		top: 50%;
	}
</style>
