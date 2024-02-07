import java.io.*;
import java.util.*;

public class Main {

  public static void main(String args[]) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    Integer CASOS = new Integer(br.readLine());
    String l = br.readLine();

    for (int c = 0; c < CASOS; c++) {

      String maiorVertice = br.readLine();

      System.out.println("V == "+(maiorVertice.charAt(0) - 'A' +1));
      Grafo G = new Grafo( (int) ( maiorVertice.charAt(0) - 'A' +1));

      while(true) {
        String aresta = br.readLine();
        if (aresta.length() == 0) break;

        System.out.print("aresta: "+ aresta);
        G.addEdge( (int)(aresta.charAt(0) - 'A'), (int)(aresta.charAt(1)-'A')); 
      }

      // Contar quantos subgrafos conexos maximais tem em G
      int contagem = G.contarSubgrafosConexosMaximais();
      /// pede impressao da contagem? 

      System.out.println(""+contagem);
      if (c < CASOS -1) {
        System.out.println("");
        l = br.readLine();
      }
    }

  }
}

class Grafo {

  boolean marked[];
  boolean[][] MA;
  int V;

  public Grafo(int V) {
    this.V = V;
    marked = new boolean[V+1];
    MA = new boolean[V+1][V+1];
  }

  public void addEdge(int u, int v) {
    MA[u][v] = MA[v][u] = true;
  }

  // versao 1: DFS
  public int contarSubgrafosConexosMaximais() {
    int numeroDeSubgrafosMaximais = 0;

    for (int v = 0; v < V; v++) {
      if (!marked[v]) {
        dfs(v);
        numeroDeSubgrafosMaximais++;
      }
    }
    return numeroDeSubgrafosMaximais;
  }

  List<Integer> adj(int s) { // na MA, custo eh O(V)
    ArrayList<Integer> a = new ArrayList<>();
    for (int v = 0; v < V; v++) {
      if (MA[s][v] == true) a.add(v);
    }
    return a;
  }

  void dfs(int s) {

    marked[s] = true;

    for (int v: adj(s)) {
      if (!marked[v]) {
        dfs(v);
      }

    }
  }

}


