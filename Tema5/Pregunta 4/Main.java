import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) throws Exception {
        if (args.length == 0) return;
        
        // Lee el archivo que le pasa el script de Python
        CharStream input = CharStreams.fromPath(Paths.get(args[0]));
        
        // Instancia el Lexer y Parser generados por ANTLR
        DockerComposeLexer lexer = new DockerComposeLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        DockerComposeParser parser = new DockerComposeParser(tokens);
        
        // Inicia el análisis desde la regla principal 'compose'
        parser.compose(); 
    }
}