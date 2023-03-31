package lexer;

public enum Tag {
    PROGRAM("PROGRAM"),
    BEGIN("BEGIN"), END("END"),
    ASSIGN("ASSIGN"),
    SUM("SUM"), SUB("SUB"), MUL("MUL"),
    OR("OR"),
    LT("LT"), LE("LE"), GT("GT"), GE("GE"),
    SEMI("SEMI"),
    LPAR("LPAR"), RPAR("RPAR"),
    ID("ID"),
    LIT_INT("LIT_INT"),
    EOF("EOF"), UNK("UNK");

    private String name;

    private Tag(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return name;
    }
}
