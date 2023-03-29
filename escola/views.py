from rest_framework import viewsets, generics
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from escola.models import Aluno, Curso, Matricula
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo Alunos e Alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo Cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo Matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as Matriculas de um Aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando Alunos Matriculados"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer

