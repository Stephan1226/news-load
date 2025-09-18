#!/bin/bash

echo "🚀 뉴스 크롤링 서비스를 시작합니다..."

# 가상환경이 존재하는지 확인
if [ ! -d "venv" ]; then
    echo "❌ 가상환경이 없습니다. 먼저 setup.sh를 실행해주세요."
    echo "   ./setup.sh"
    exit 1
fi

# 가상환경 활성화
echo "🔧 가상환경을 활성화합니다..."
source venv/bin/activate

# 서비스 시작
echo "🌐 FastAPI 서버를 시작합니다..."
echo "서버가 시작되면 다음 주소에서 접속할 수 있습니다:"
echo "  - API 문서: http://localhost:8000/docs"
echo "  - 서비스: http://localhost:8000"
echo ""
echo "종료하려면 Ctrl+C를 누르세요."
echo ""

python main.py