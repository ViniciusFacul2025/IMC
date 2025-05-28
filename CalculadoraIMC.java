import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CalculadoraIMC extends JFrame implements ActionListener {

    private JTextField campoPeso, campoAltura;
    private JButton botaoCalcular;
    private JLabel resultadoLabel;

    public CalculadoraIMC() {
        setTitle("Calculadora de IMC");
        setSize(300, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(5, 1));

        campoPeso = new JTextField();
        campoAltura = new JTextField();
        botaoCalcular = new JButton("Calcular IMC");
        resultadoLabel = new JLabel("", SwingConstants.CENTER);

        add(new JLabel("Peso (Kg):"));
        add(campoPeso);
        add(new JLabel("Altura (cm):"));
        add(campoAltura);
        add(botaoCalcular);
        add(resultadoLabel);

        botaoCalcular.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        try {
            double peso = Double.parseDouble(campoPeso.getText());
            double alturaCm = Double.parseDouble(campoAltura.getText());
            double alturaM = alturaCm / 100;
            double imc = peso / (alturaM * alturaM);

            String classificacao;
            if (imc < 18.5) {
                classificacao = "Abaixo do peso";
            } else if (imc < 24.9) {
                classificacao = "Peso normal";
            } else if (imc < 29.9) {
                classificacao = "Sobrepeso";
            } else if (imc < 34.9) {
                classificacao = "Obesidade grau 1";
            } else if (imc < 39.9) {
                classificacao = "Obesidade grau 2";
            } else {
                classificacao = "Obesidade grau 3";
            }

            resultadoLabel.setText(String.format("IMC: %.2f - %s", imc, classificacao));
        } catch (NumberFormatException ex) {
            resultadoLabel.setText("Insira valores válidos.");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            CalculadoraIMC app = new CalculadoraIMC();
            app.setVisible(true);
        });
    }
}
