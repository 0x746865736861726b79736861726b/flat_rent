async function authenticateWithMetaMask() {
    if (window.ethereum) {
        try {
            const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
            const address = accounts[0];

            const message = "Authentication message";
            const web3 = new Web3(window.ethereum);
            const signature = await web3.eth.personal.sign(message, address);

            const response = await fetch('/auth/metamask/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ address, signature, message }),
            });

            const data = await response.json();
            if (data.success && data.redirect_url) {
                console.log('Аутентифікація успішна!');
                window.location.href = data.redirect_url;
            } else {
                console.log('Аутентифікація не вдалася');
            }
        } catch (error) {
            console.error('Помилка MetaMask:', error);
        }
    } else {
        console.log('MetaMask не встановлено');
    }
}