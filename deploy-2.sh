for CHALL_DIR in "Binary Exploitation/Calculator" "Cryptography/CryptoVault/" "Web Exploitation/indexphpts/"
do
    echo "ZCZC DIR $CHALL_DIR"
    pushd "$CHALL_DIR"
        echo "ZCZC EXEC docker compose $@"
        docker compose $@
    popd
done
