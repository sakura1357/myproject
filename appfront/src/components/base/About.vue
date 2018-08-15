<template>
	<div id="about">
		<p>{{ msg }}</p>
	</div>
</template>
<script>
	export default {
		name:'About',
		data(){
			return {
				msg: '我是About组件'
			}
		}
	}
</script>