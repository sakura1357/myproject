<template>
	<div id="home">
		<p>{{ msg }}</p>
	</div>
</template>
<script type="text/javascript">
	export default {
		name: 'home',
		data(){
			return {
				msg: "我是home组件"
			}
		}
	}
</script>