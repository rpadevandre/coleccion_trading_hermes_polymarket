import { useMemo, useState } from 'react';
import type { ComponentType } from 'react';
import Landing from './views/Landing';
import ReportBeforeAfter from './views/ReportBeforeAfter';
import ClientProofDemo from './views/ClientProofDemo';
import StackAuditForm from './views/StackAuditForm';
import PilotSignup from './views/PilotSignup';
import { businessMeta, frontendViews, RouteKey } from './businessMeta';
import './styles.css';

export type ViewProps = {
  onNavigate: (route: RouteKey, intent?: string) => void;
};

const routeComponents: Record<RouteKey, ComponentType<ViewProps>> = {
  landing: Landing,
  'report-before-after': ReportBeforeAfter,
  'client-proof-demo': ClientProofDemo,
  'stack-audit-form': StackAuditForm,
  'pilot-signup': PilotSignup,
};

export default function App() {
  const [route, setRoute] = useState<RouteKey>('landing');
  const [lastIntent, setLastIntent] = useState('Evaluating whether security reporting is painful enough to fix');
  const ActiveView = useMemo(() => routeComponents[route], [route]);
  const activeMeta = frontendViews.find((view) => view.key === route) ?? frontendViews[0];

  const navigate = (nextRoute: RouteKey, intent?: string) => {
    if (intent) setLastIntent(intent);
    setRoute(nextRoute);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="app-shell">
      <nav className="top-nav" aria-label="Prototype views">
        <div className="brand-block">
          <strong>{businessMeta.name}</strong>
          <span>{businessMeta.buyer}</span>
        </div>
        <div className="nav-buttons" role="list">
          {frontendViews.map((view) => (
            <button
              key={view.key}
              type="button"
              onClick={() => navigate(view.key)}
              className={route === view.key ? 'active' : ''}
              aria-current={route === view.key ? 'page' : undefined}
            >
              {view.navLabel}
            </button>
          ))}
        </div>
      </nav>

      <aside className="route-context" aria-live="polite">
        <span>Current validation step:</span>
        <strong>{activeMeta.primaryOutcome}</strong>
        <em>{lastIntent}</em>
      </aside>

      <ActiveView onNavigate={navigate} />
    </div>
  );
}
