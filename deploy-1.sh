for CHALL_DIR in "Binary Exploitation/SMS" "Binary Exploitation/Working at Compfest Shop" "Cryptography/choose exponent/" "Misc/napi/" "Web Exploitation/compaste/" "Web Exploitation/reader2/"
do
    echo "ZCZC DIR $CHALL_DIR"
    pushd "$CHALL_DIR"
        echo "ZCZC EXEC docker compose $@"
        docker compose $@
    popd
done
