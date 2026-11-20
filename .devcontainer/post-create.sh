#!/usr/bin/env bash
# Instala as ferramentas que não têm "feature" oficial e mostra as versões.
set -euo pipefail

case "$(uname -m)" in
  x86_64)  ARCH=amd64 ;;
  aarch64) ARCH=arm64 ;;
  *) echo "Arquitetura não suportada: $(uname -m)"; exit 1 ;;
esac

echo "==> uv (gerenciador de pacotes Python)"
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "==> kind (Kubernetes local dentro do Docker)"
sudo curl -fsSLo /usr/local/bin/kind \
  "https://github.com/kubernetes-sigs/kind/releases/latest/download/kind-linux-${ARCH}"
sudo chmod +x /usr/local/bin/kind

echo "==> k9s (painel de terminal para Kubernetes)"
curl -fsSL "https://github.com/derailed/k9s/releases/latest/download/k9s_Linux_${ARCH}.tar.gz" \
  | sudo tar -xz -C /usr/local/bin k9s

echo "==> argocd CLI"
sudo curl -fsSLo /usr/local/bin/argocd \
  "https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-${ARCH}"
sudo chmod +x /usr/local/bin/argocd

export PATH="$HOME/.local/bin:$PATH"

echo
echo "==> Ferramentas instaladas:"
echo "python:    $(python --version)"
echo "uv:        $(uv --version)"
echo "node:      $(node --version)"
echo "npm:       $(npm --version)"
echo "docker:    $(docker --version)"
echo "terraform: $(terraform version | head -n1)"
echo "kubectl:   $(kubectl version --client 2>/dev/null | head -n1)"
echo "helm:      $(helm version --short)"
echo "kind:      $(kind version)"
echo "k9s:       $(k9s version --short 2>/dev/null | head -n1)"
echo "argocd:    $(argocd version --client --short 2>/dev/null)"
echo "aws:       $(aws --version)"
echo "gh:        $(gh --version | head -n1)"
