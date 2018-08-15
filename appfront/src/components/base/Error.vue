<template>
	<div id="error">
		<p>{{ msg }}</p>
	</div>
</template>
<script>
	export default {
		name: 'Error',
		data (){
			return {
				msg: "这是error页面"
			}
		}
	}
</script>