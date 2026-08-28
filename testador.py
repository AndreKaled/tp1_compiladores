import random
import subprocess
import re

PROTOCOLS = ["http://", "https://", "ftp://"]
DOMAINS = ["example.com", "site.org.br", "api.sub.domain.net"]
PORTS = [":80", ":443", ":8080", ":3000"]
PATHS = ["/index.html", "/api/v1/users", "/images/logo.png", "/docs"]
QUERIES = ["?id=123", "?search=test&page=2", "?sort=asc&filter=all"]
FRAGMENTS = ["#top", "#section1", "#footer"]

def generate_case(should_be_valid: bool) -> str:
    if should_be_valid:
        proto = random.choice(PROTOCOLS) if random.random() > 0.4 else ""
        domain = random.choice(DOMAINS)
        port = random.choice(PORTS) if random.random() > 0.5 else ""
        path = random.choice(PATHS) if random.random() > 0.4 else ""
        query = random.choice(QUERIES) if random.random() > 0.5 else ""
        frag = random.choice(FRAGMENTS) if random.random() > 0.5 else ""
        return f"{proto}{domain}{port}{path}{query}{frag}"
    else:
        corruptions = [
            f"gopher://{random.choice(DOMAINS)}",
            f"{random.choice(PROTOCOLS)}dominio com espaco.com",
            f"{random.choice(PROTOCOLS)}{random.choice(DOMAINS)}:invalid_port",
            f"{random.choice(PROTOCOLS)}{random.choice(DOMAINS)}/caminho com espaço",
            f"{random.choice(PROTOCOLS)}{random.choice(DOMAINS)}?parametro_sem_igual",
            "://sem_dominio.com",
            "apenas_texto_sem_ponto",
        ]
        return random.choice(corruptions)

def parse_tokens(output: str) -> list[tuple[str, str]]:
    """Extrai pares (TOKEN, VALOR) ignorando mensagens de log do docker/build."""
    tokens = re.findall(r"TOKEN:\s*(\w+)\s*\nVALOR:\s*([^\n]+)", output)
    return tokens

def run_test(url: str) -> list[tuple[str, str]]:
    cmd = ["docker", "compose", "run", "--rm", "antlr", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return parse_tokens(result.stdout)

def main(total_cases: int = 15):
    passed = 0
    results = []

    for i in range(1, total_cases + 1):
        expected_valid = random.choice([True, False])
        test_url = generate_case(expected_valid)
        
        tokens = run_test(test_url)
        
        # Considera URL válida APENAS se houver 1 único token URL que consumiu a string inteira
        is_full_url = len(tokens) == 1 and tokens[0][0] == "URL" and tokens[0][1] == test_url
        
        test_ok = (is_full_url == expected_valid)
        if test_ok:
            passed += 1

        results.append({
            "id": i,
            "status": "PASS" if test_ok else "FAIL",
            "expected": "VÁLIDO" if expected_valid else "INVÁLIDO",
            "url": test_url,
            "tokens": tokens
        })

    # Exibição organizada
    print(f"\n{'ID':<4} {'STATUS':<6} {'ESPERADO':<10} {'URL'}")
    print("-" * 75)
    for r in results:
        print(f"{r['id']:<4} {r['status']:<6} {r['expected']:<10} {r['url']}")
        if r['status'] == "FAIL":
            tokens_str = ", ".join([f"{t[0]}('{t[1]}')" for t in r['tokens']]) if r['tokens'] else "Nenhum token reconhecido"
            print(f"     └── Tokens emitidos: {tokens_str}")

    print("-" * 75)
    print(f"Total: {passed}/{total_cases} testes passaram.\n")

if __name__ == "__main__":
    main()