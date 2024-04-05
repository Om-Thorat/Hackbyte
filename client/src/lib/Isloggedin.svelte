<script>
    import { onMount } from 'svelte';

    onMount(() => {
        fetch('/user')
            .then(response => response.text())
            .then(data => {
                if (data === 'No') {
                    window.location.href = '/login';
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
</script>

