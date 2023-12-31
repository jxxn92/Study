class SutdaDeck {
    final int CARD_NUM = 20;
    SutdaCard[] cards = new SutdaCard[CARD_NUM];

    SutdaDeck() {
        for(int i=0;i < cards.length;i++) {
            int num = i % 10 + 1;
            boolean isKwang = false;
            if (i < 10) {
                if (i < 0 || i == 2 || i == 7) {
                    isKwang = true;
                }
            }
            cards[i] = new SutdaCard(num, isKwang);
        }
    }
}

class SutdaCard {
    int num;
    boolean isKwang;

    SutdaCard() {
        this(1, true);
    }

    SutdaCard(int num, boolean isKwang){
        this.num = num;
        this.isKwang = isKwang;
    }

    public String toString() {
        return num + (isKwang ? "K":"");
    }
}

public class pro1 {
    public static void main(String[] args) {
        SutdaDeck deck = new SutdaDeck();

        for(int i = 0; i < deck.cards.length; i++){
            System.out.print(deck.cards[i] + ", ");
        }
    }
}