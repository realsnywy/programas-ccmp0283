# Análise e Solução de Exceptions em Código

Esta atividade visa desenvolver a capacidade de identificar, corrigir e prevenir exceções comuns em Java. Os alunos devem criar programas que gerem erros específicos e, em seguida, implementar soluções robustas.

## Exceções Abordadas

Utilizando 5 das exceções mais frequentes no desenvolvimento Java:

- `NullPointerException`
- `NumberFormatException`
- `IllegalArgumentException`
- `RuntimeException`
- `IllegalStateException`

## Estrutura do Trabalho

Para cada exceção, apresentar:

1. **Código com o Bug**: Trecho que provoque o erro.
2. **Explicação Técnica**: Contexto e causa raiz do erro.
3. **Código Corrigido**: Solução com tratamento adequado.
4. **Prevenção**: Boas práticas para evitar a exceção.

## Exemplos Práticos (Modelo)

### 1. NullPointerException

**Objetivo**: Acessar um método de um objeto não inicializado.

**Código com Bug**:

```java
public class ExemploNPE {  
    public static void main(String[] args) {  
        String texto = null;  
        System.out.println(texto.length()); // Gera NullPointerException  
    }  
}  
```

**Correção**:

```java
public class ExemploNPE {  
    public static void main(String[] args) {  
        String texto = null;  
        if (texto != null) {  
            System.out.println(texto.length());  
        } else {  
            System.out.println("Texto não inicializado.");  
        }  
    }  
}
```

## Critérios de Avaliação

1. **Clareza**: Código bem documentado e explicado.
2. **Correção**: Solução resolve o erro eficientemente.
3. **Prevenção**: Uso de boas práticas para evitar recorrência.
4. **Criatividade**: Complexidade adequada dos exemplos.

## Entrega

- Dois arquivos por exceção (bug e correção).
- Relatório resumido com análise de cada caso.
- Compactar em um único arquivo e submeter na atividade.

## Dicas Gerais

- Use `try-catch` para exceções verificáveis.
- Valide entradas de usuário e parâmetros de métodos.
- Utilize ferramentas como `Optional` e `Objects.requireNonNull()`.
- Evite `RuntimeException` para erros recuperáveis.

Esta estrutura promove a compreensão prática de exceções e fortalece habilidades de depuração em Java.

## Apresentação

A atividade será apresentada em sala para colaboração com a turma.
