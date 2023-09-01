for CHALL_DIR in "Binary Exploitation/Greetify v2" "Web Exploitation/noobgramer/"
do
    echo "ZCZC DIR $CHALL_DIR"
    pushd "$CHALL_DIR"
        echo "ZCZC EXEC docker compose $@"
        docker compose $@
    popd
done
