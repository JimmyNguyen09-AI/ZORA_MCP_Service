from app.models import OwnerInfoResponse


class OwnerService:
    """
    Service trả về thông tin chủ sở hữu / creator của ZORA (static)
    """
    def get_owner_info(self) -> OwnerInfoResponse:
        return OwnerInfoResponse(
            success=True,
            name="Nguyễn Trung Thành (Jimmy Nguyen)",
            phone="0432047700",
            email="ng.trungthanh04@gmail.com",
            role="AI Developer & Software Engineer",
            bio=(
                "Nguyễn Trung Thành, biệt danh Jimmy Nguyen, sinh ngày 09/12/2004, quê quán Hải Phòng(Việt Nam), hiện đang sinh sống và làm việc tại Sydney(Úc), là 1 genAI Engineer với 1 niềm đam mê mãnh liệt về AI và phát triển phần mềm."
            ),
            skills=[
                "Python",
                "FastAPI",
                "Pytorch",
                "Computer Vison",
                "Next.JS",
                "Node.JS",
                "LangChain",
                "Machine Learning",
                "Natural Language Processing",
                "RAG Systems",
                "PostgreSQL",
                "Docker",
                "MCP Protocol",
            ],
        )
